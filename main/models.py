from django.db import models

# Create your models here.
STATUS = ((0, "Draft"), (1, "Published"))
class Project(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, unique=True)
    text = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    class Meta:
        ordering=("-created_at",)
        
    def __str__(self):
        return self.title
    
class Structure(models.Model):
    full_name = models.CharField(max_length=120)
    image = models.ImageField(upload_to='person_images/')
    post = models.CharField(max_length=50)
    text = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    
    def remove_on_image_update(self):
        try:
            # is the object in the database yet?
            obj = Structure.objects.get(id=self.id)
        except Structure.DoesNotExist:
            # object is not in db, nothing to worry about
            return
        # is the save due to an update of the actual image file?
        if obj.image and self.image and obj.image != self.image:
            # delete the old image file from the storage in favor of the new file
            obj.image.delete()

    def delete(self, *args, **kwargs):
        # object is being removed from db, remove the file from storage first
        self.image.delete()
        return super(Structure, self).delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        # object is possibly being updated, if so, clean up.
        self.remove_on_image_update()
        return super(Structure, self).save(*args, **kwargs)
    
    class Meta:
        ordering=("-created_at",)
        
    def __str__(self):
        return self.full_name
    