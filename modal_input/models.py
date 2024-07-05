from django.db import models


class modalInput(models.Model):

    title = models.CharField(max_length=200)
    description = models.TextField()
    last_modified = models.DateTimeField()
    slug = models.SlugField(max_length=200)
    auto_field = models.AutoField(primary_key=True)
    # big_auto_field = models.BigAutoField(primary_key=True)
    big_integer_field = models.BigIntegerField()
    binary_field = models.BinaryField()
    boolean_field = models.BooleanField()
    char_field = models.CharField(max_length=255)
    # comma_separated_field = models.CharField(
    #     validators=[comma_separated_validator],
    #     max_length=255
    # )
    date_field = models.DateField()
    date_time_field = models.DateTimeField()
    decimal_field = models.DecimalField(max_digits=5, decimal_places=2)

    email_field = models.EmailField()
    file_field = models.FileField(upload_to='files/')
    file_field1 = models.FileField(upload_to='files/')
    generic_ip_address_field = models.GenericIPAddressField()
    image_field = models.ImageField(upload_to='images/')
    integer_field = models.IntegerField()
    json_field = models.JSONField()
    text_field = models.TextField()
    time_field = models.TimeField()
    url_field = models.URLField()



    positive_big_integer_field = models.PositiveBigIntegerField()


# img = models.ImageField(upload_to = "images/")
