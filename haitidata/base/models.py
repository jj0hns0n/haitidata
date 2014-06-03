from datetime import datetime 
import os 
import hashlib 

from django.db import models 
from django.contrib.auth.models import User 
from django.utils.translation import ugettext_lazy as _ 
from django.core.exceptions import ValidationError, ObjectDoesNotExist 
from django.core.files.base import ContentFile 
from django.conf import settings 
from django.contrib.staticfiles.templatetags import staticfiles 

from geonode.base.enumerations import COUNTRIES, ALL_LANGUAGES, \
    HIERARCHY_LEVELS, UPDATE_FREQUENCIES, CONSTRAINT_OPTIONS, \
    SPATIAL_REPRESENTATION_TYPES, \
    DEFAULT_SUPPLEMENTAL_INFORMATION, LINK_TYPES 
from geonode.utils import bbox_to_wkt 
from geonode.people.models import Profile, Role 
from geonode.security.models import PermissionLevelMixin 

from taggit.managers import TaggableManager

from geonode.base.models import TopicCategory

class TopicCategoryGroup(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField()
    description = models.TextField(blank=True)
    def __unicode__(self):
        return u"{0}".format(self.name)
    @property
    def links(self):
        return self.topiccategorygrouplink_set.all()
    @property
    def counts(self):
        counts = {
            'layers': 0,
            'maps': 0,
            'documents': 0
        }
        for categorylink in self.links:
            for resource in categorylink.base_topiccategory.resourcebase_set.all():
                try:
                    resource.layer
                    counts['layers'] += 1
                except ObjectDoesNotExist:
                    pass
                try:
                    resource.map
                    counts['maps'] += 1
                except ObjectDoesNotExist:
                    pass
                try:
                    resource.document
                    counts['documents'] += 1
                except ObjectDoesNotExist:
                    pass
        return counts
    class Meta:
        ordering = ("name",)
        verbose_name_plural = 'Topic Category Groups'


class TopicCategoryGroupLink(models.Model):
    base_topiccategorygroup = models.ForeignKey(TopicCategoryGroup)
    base_topiccategory = models.ForeignKey(TopicCategory)
    def __unicode__(self):
        return str(self.id)
    class Meta:
        verbose_name_plural = 'Topic Category Group Links'

