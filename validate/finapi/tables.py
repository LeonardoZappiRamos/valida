import django_tables2 as tables

class ValueColumn(tables.Column):
    def render(self, record):
        return "u$ {:.2f}".format(record.first_name, record.last_name)
      
class StockTable(tables.Table):
  stock = tables.Column(attrs={'class': 'col'})
  name = tables.Column()
  close = tables.Column()
  sector = tables.Column()
  
  class Meta:
    template_name = "django_tables2/bootstrap4.html"
    attrs = {
      "class": "table",
    }