from django.contrib import admin

from haitidata.base.models import TopicCategoryGroup, TopicCategoryGroupLink

class TopicCategoryGroupAdmin(admin.ModelAdmin):
    model = TopicCategoryGroup
    list_display_links = ('name',)
    list_display = ('id', 'name', 'slug', 'description')

class TopicCategoryGroupLinkAdmin(admin.ModelAdmin):
    model = TopicCategoryGroupLink
    list_display_links = ('id','base_topiccategory',)
    list_display = ('id','base_topiccategory','base_topiccategorygroup',)

admin.site.register(TopicCategoryGroup, TopicCategoryGroupAdmin)
admin.site.register(TopicCategoryGroupLink, TopicCategoryGroupLinkAdmin)

