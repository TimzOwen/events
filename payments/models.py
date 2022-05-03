from pyexpat import model


class Payments(model.Model):
    name = model.CharField()
    phone = model.IntegerField()
    amount = model.IntegerField()

    def __str__(self):
        return self.name

class Cashflow(model.Model):
    total_amount = model.IntegerField()
    
