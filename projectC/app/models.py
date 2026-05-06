from django.db import models

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=225)
    lastname = models.CharField(max_length=225)
    email = models.EmailField(unique=True)
    usertype = models.CharField(max_length=225)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"


class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Client {self.client_id}"


class Provider(models.Model):
    provider_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    travel_radius = models.IntegerField()
    background_check_status = models.CharField(max_length=225)
    rating = models.DecimalField(max_digits=3, decimal_places=2)

    def __str__(self):
        return f"Provider {self.provider_id}"


class ServiceCategory(models.Model):
    service_category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=225)

    def __str__(self):
        return self.category_name


class JobRequest(models.Model):
    job_id = models.AutoField(primary_key=True)
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    category_id = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE)
    description = models.TextField()
    location = models.CharField(max_length=225)
    status = models.CharField(max_length=20)

    def __str__(self):
        return f"Job {self.job_id}"


class JobAssignment(models.Model):
    assignment_id = models.AutoField(primary_key=True)
    job_id = models.ForeignKey(JobRequest, on_delete=models.CASCADE)
    provider_id = models.ForeignKey(Provider, on_delete=models.CASCADE)
    agreed_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Assignment {self.assignment_id}"


class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    job_id = models.ForeignKey(JobRequest, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Payment {self.payment_id}"


class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    job_id = models.ForeignKey(JobRequest, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comments = models.TextField()

    def __str__(self):
        return f"Review {self.review_id}"