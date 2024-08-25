import markdown
from django import template
from django.db.models import Count
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe
from taggit.models import Tag

from ..models import Post

register = template.Library()


@register.simple_tag
def total_posts():
    return Post.published.count()


@register.simple_tag
def total_tags():
    return Tag.objects.count()


@register.inclusion_tag("blog/post/latest_posts.html")
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by("-publish")[:count]
    return {"latest_posts": latest_posts}


@register.simple_tag
def get_most_commented_posts(count=5):
    return Post.published.annotate(total_comments=Count("comments")).order_by(
        "-total_comments"
    )[:count]


@register.filter(name="markdown")
def markdown_format(text):
    return mark_safe(
        markdown.markdown(
            text, extensions=["tables", "fenced_code", "codehilite"]
        )
    )


@register.filter(is_safe=False)
@stringfilter
def pluralize(value, forms):
    """
    Подбирает окончание существительному после числа
    {{someval|pluralize:"товар,товара,товаров"}}
    """
    try:
        one, two, many = forms.split(",")
        value = str(value)[-2:]  # 314 -> 14

        if 21 > int(value) > 4:
            return many

        if value.endswith("1"):
            return one
        elif value.endswith(("2", "3", "4")):
            return two
        else:
            return many

    except (ValueError, TypeError):
        return ""
