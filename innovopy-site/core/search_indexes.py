# search_indexes.py

from haystack import indexes
from asset.models import Asset


class AssetIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')
    room = indexes.CharField(model_attr='room', default='', faceted=True)
    short_desc = indexes.CharField(model_attr='short_desc', default='')
    full_desc = indexes.CharField(model_attr='full_desc', default='')
    contact_1_name = indexes.CharField(model_attr='contact_1_name', default='')
    manufacturer = indexes.CharField(model_attr='manufacturer', default='')


    def get_model(self):
        return Asset

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()