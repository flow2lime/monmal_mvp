from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = "category"

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name       = models.CharField(max_length=50)
    category_id = models.ForeignKey("category", on_delete=models.CASCADE, related_name="subcategory")
    
    class Meta:
        db_table = "subcategory"

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50)
    
    class Meta:
        db_table = "tag"

    def __str__(self):
        return self.name

class Text(models.Model):
    name          = models.CharField(max_length=50)
    category_id    = models.ForeignKey("category", on_delete=models.CASCADE, related_name="text")
    subCategory_id = models.ForeignKey("subcategory", on_delete=models.CASCADE, related_name="text")
    tag           = models.ForeignKey("tag", on_delete=models.CASCADE, related_name="text")
    
    class Meta:
        db_table = "text"

    def __str__(self):
        return self.name


class Chunk(models.Model):
    name = models.CharField(max_length=50)
    
    class Meta:
        db_table = "chunk"

    def __str__(self):
        return self.name

class TextToChunk(models.Model):
    text_id  = models.ForeignKey("text", on_delete=models.CASCADE, related_name="text_to_chunk")
    chunk_id = models.ForeignKey
    order   = models.IntegerField()
    
    class Meta:
        db_table = "text_to_chunk"

    def __str__(self):
        return self.name


class Dictionary(models.Model):
    chunk_id    = models.ForeignKey("chunk", on_delete=models.CASCADE, related_name="dictionary")
    lemma      = models.CharField(max_length=50)
    definition = models.CharField(max_length=500)

    
    class Meta:
        db_table = "dictionary"

    def __str__(self):
        return self.name