from main.settings import data_base

class Tour(data_base.Model):
    id = data_base.Column(data_base.Integer, primary_key = True)
    title = data_base.Column(data_base.String(60), nullable = False)
    date = data_base.Column(data_base.String(60), nullable = False)
    country = data_base.Column(data_base.String(60), nullable = False)
    price = data_base.Column(data_base.String(60), nullable = False)
    description = data_base.Column(data_base.String(60), nullable = False)

    def __repr__(self) -> str:
        return f"Тур {self.title}"