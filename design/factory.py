import abc
import html
import os


class AbstractFormBuilder(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def add_title(self, title):
        self.title = title

    @abc.abstractmethod
    def add_label(self, text, row, column, **kwargs):
        pass

    @abc.abstractmethod
    def add_button(self, text, row, column, **kwargs):
        pass

    def add_entry(self, variable, row, column, **kwargs):
        pass

    def form(self):
        pass


class HtmlFormBuilder(AbstractFormBuilder):
    def __init__(self):
        self.title = 'HtmlFormBuilder'
        self.items = {}

    def add_title(self, title):
        super(HtmlFormBuilder, self).add_title(title)

    def add_label(self, text, row, column, **kwargs):
        self.items[(row, column)] = ('<td><label for="{}">{}:</label></td>'
                                     .format(kwargs['target'], html.escape(text)))

    def add_button(self, text, row, column, **kwargs):
        self.items[(row, column)] = '<td><input type="button" value="{}"></td>'.format(text)

    def add_entry(self, variable, row, column, **kwargs):
        html = '''<td><input name="{}" type="{}"></td>'''.format(variable, kwargs.get("kind", "text"))
        self.items[(row, column)] = html

    def form(self):
        html = ['<!DOCTYPE html>\n<html lang="en"><head><meta charset="UTF-8"><title>{}</title></head><body>'.format(
            self.title),
            '<form><table border="0">']
        this_row = None
        for key, value in self.items.items():
            row, column = key
            if this_row is None:
                html.append('<tr>')
            elif this_row != row:
                html.append('</tr>\n <tr>')
            this_row = row
            html.append('   ' + value)
        html.append('</tr></table></form></body></html>')
        return '\n'.join(html)


class TkFormBuilder(AbstractFormBuilder):
    pass


def create_login_form(builder):
    builder.add_title('Login')
    builder.add_label('Username', 0, 0, target='username')
    builder.add_entry('username', 0, 1)
    return builder.form()


htmlform = create_login_form(HtmlFormBuilder())
path = os.path.dirname(os.path.abspath(__file__))
with open('demo.html', 'w', encoding='utf-8') as f:
    f.write(htmlform)
