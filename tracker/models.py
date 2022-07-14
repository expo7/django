from django.db import models
from django.utils.text import slugify
FAT=9
CARB=4
PROTEIN=4

class  Food(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(blank=True, null=True)
    servingSize=models.CharField(max_length=300)
    Fat = models.FloatField()
    Protein = models.FloatField()
    Carbohydrates=models.FloatField() #
    Calories = models.FloatField(blank=True, null=True)
    percentFat = models.FloatField(blank=True, null=True)
    percentProtein = models.FloatField(blank=True, null=True)
    percentCarbohydrates=models.FloatField(blank=True, null=True)

    
    Fiber = models.FloatField(blank=True, null=True)
    netCarbohydrates = models.FloatField()
    text1=models.TextField(max_length=2000,blank=True,null=True)   
    text2=models.TextField(max_length=2000,blank=True,null=True)   
    text3=models.TextField(max_length=2000,blank=True,null=True)   
    text4=models.TextField(max_length=2000,blank=True,null=True)   
    text5=models.TextField(max_length=2000,blank=True,null=True)   
    text6=models.TextField(max_length=2000,blank=True,null=True)   
    text7=models.TextField(max_length=2000,blank=True,null=True)      
    text8=models.TextField(max_length=2000,blank=True,null=True)   
    text9=models.TextField(max_length=2000,blank=True,null=True)   
    text10=models.TextField(max_length=2000,blank=True,null=True)   
    subtitle = models.CharField(max_length=300 ,null=True, blank=True)
    slug = models.SlugField(blank=True,null=True) 
    def __str__(self):
      return self.name

    def get_absolute_url(self):
        return reverse("food_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        cf=self.Fat*FAT
        cc=self.Carbohydrates*CARB 
        cp=self.Protein*PROTEIN
        self.Calories=cf+cc+cp
        self.netCarbohydrates=self.Carbohydrates-self.Fiber
        self.percentCarbohydrates=(cc/self.Calories)*100
        self.percentFat=(cf/self.Calories)*100
        self.percentProtein=(cp/self.Calories)*100
        self.slug = slugify(self.name)
        super(Food, self).save(*args, **kwargs)



class  Article(models.Model):
    title = models.CharField(max_length=300)
    pub_date = models.DateField()
    subtitle = models.CharField(max_length=300 ,null=True, blank=True)
    subtitle2 = models.CharField(max_length=300, null=True, blank=True)
    subtitle3 = models.CharField(max_length=300, null=True, blank=True)
    subtitle4 = models.CharField(max_length=300, null=True, blank=True)
    subtitle5 = models.CharField(max_length=300 ,null=True, blank=True)
    subtitle6 = models.CharField(max_length=300, null=True, blank=True)
    text2=models.TextField(max_length=1000, null=True, blank=True)
    image = models.ImageField()
    text1=models.TextField(max_length=1000, null=True, blank=True)
    text2=models.TextField(max_length=1000, null=True, blank=True)
    text3=models.TextField(max_length=1000, null=True, blank=True)
    text4=models.TextField(max_length=1000, null=True, blank=True)
    text4=models.TextField(max_length=1000, null=True, blank=True)
    text5=models.TextField(max_length=1000, null=True, blank=True)
    text6=models.TextField(max_length=1000, null=True, blank=True)
    text7=models.TextField(max_length=1000,null=True, blank=True)
    text8=models.TextField(max_length=1000,null=True, blank=True)
    text9=models.TextField(max_length=1000,null=True, blank=True)
    text10=models.TextField(max_length=1000,null=True, blank=True)
    text11=models.TextField(max_length=1000, null=True, blank=True)
    text12=models.TextField(max_length=1000,null=True, blank=True)
    text13=models.TextField(max_length=1000,null=True, blank=True)
    text14=models.TextField(max_length=1000,null=True, blank=True)
    text15=models.TextField(max_length=1000,null=True, blank=True)
    slug = models.SlugField(blank=True,null=True) 
    def __str__(self):
      return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
      
        super(Article, self).save(*args, **kwargs)



class Product(models.Model):
    name = models.CharField(max_length=300)
    # articles2 = models.ManyToManyField(Article, related_name='articles',null=True, blank=True)
    image = models.ImageField(default='default.jpg', upload_to='product_pics')
    price = models.FloatField()
    articles=models.ManyToManyField(Article, related_name='articles',blank=True)
    link= models.CharField(max_length=300)
    discription=models.TextField(max_length=2000)


    def __str__(self):
      return self.name

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'pk': self.pk})