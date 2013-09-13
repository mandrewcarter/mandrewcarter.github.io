from docutils.parsers.rst import Directive as _Directive
from docutils.parsers.rst import Parser as _Parser
from docutils.parsers.rst.directives.body import Container as _Container
from docutils.parsers.rst.directives.tables import Table as _Table
from docutils.parsers.rst.directives.tables import ListTable as _ListTable
from docutils.parsers.rst.directives.misc import Raw as _Raw
from docutils import nodes as _nodes
from docutils.statemachine import ViewList as _ViewList

import libdev.util.util as _libdevutil
import libdev.template.tempy as _tempy
import yaml as _yaml
import libdev.sh as _sh

def setup(app):

    app.add_directive('data-table', DataTable)

    app.add_javascript('jquery.js')
    app.add_javascript('jquery.dataTables.js')

    app.add_stylesheet('datatable.css')


class DataTable(_ListTable):

    # this enables content in the directive
    has_content = True

    required_arguments = 0

    count = 0

    def run(self):

        css_class = list(self.options.get('class', ()))

        table_class = 'datatable_%d' % self.count

        css_class = css_class + [table_class, 'display']

        self.options['class'] = css_class

        text = _table_java_script_call % table_class

        raw_node = _nodes.raw('', text, format='html')

        return super(DataTable, self).run() + [raw_node]


_table_java_script_call = """
<!---
https://datatables.net/release-datatables/examples/basic_init/filter_only.html
--->
<script type="text/javascript" charset="utf-8">
    $(document).ready(function() {
        $('.%s').dataTable( {
            "bPaginate": false,
            "bLengthChange": false,
            "bFilter": true,
            "bSort": true,
            "bInfo": false,
            "bAutoWidth": false
        } );
    } );
</script>
"""


