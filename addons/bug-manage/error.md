錯誤:
Odoo Server Error

Traceback (most recent call last):
  File "/usr/src/app/odoo/addons/base/models/ir_ui_view.py", line 392, in _check_xml
    self.postprocess_and_fields(view.model, view_doc, view.id)
  File "/usr/src/app/odoo/addons/base/models/ir_ui_view.py", line 931, in postprocess_and_fields
    self.raise_view_error(_('Model not found: %(model)s') % dict(model=model), view_id)
  File "/usr/src/app/odoo/addons/base/models/ir_ui_view.py", line 592, in raise_view_error
    raise ValueError(message)
ValueError: 沒有找到模型: bm.bug

錯誤的上下文:
視圖 `bug列表`
[view_id: 567, xml_id: n/a, model: bm.bug, parent_id: n/a]

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/usr/src/app/odoo/tools/convert.py", line 713, in parse
    self._tag_root(de)
  File "/usr/src/app/odoo/tools/convert.py", line 675, in _tag_root
    f(rec)
  File "/usr/src/app/odoo/tools/convert.py", line 675, in _tag_root
    f(rec)
  File "/usr/src/app/odoo/tools/convert.py", line 578, in _tag_record
    record = model._load_records([data], self.mode == 'update')
  File "/usr/src/app/odoo/models.py", line 4062, in _load_records
    records = self._load_records_create([data['values'] for data in to_create])
  File "/usr/src/app/odoo/addons/website/models/ir_ui_view.py", line 148, in _load_records_create
    records = super(View, self)._load_records_create(values)
  File "/usr/src/app/odoo/models.py", line 3976, in _load_records_create
    return self.create(values)
  File "<decorator-gen-31>", line 2, in create
  File "/usr/src/app/odoo/api.py", line 344, in _model_create_multi
    return create(self, arg)
  File "/usr/src/app/odoo/addons/base/models/ir_ui_view.py", line 473, in create
    return super(View, self).create(vals_list)
  File "<decorator-gen-3>", line 2, in create
  File "/usr/src/app/odoo/api.py", line 344, in _model_create_multi
    return create(self, arg)
  File "/usr/src/app/odoo/models.py", line 3757, in create
    fields[0].determine_inverse(batch_recs)
  File "/usr/src/app/odoo/fields.py", line 1096, in determine_inverse
    getattr(records, self.inverse)()
  File "/usr/src/app/odoo/addons/base/models/ir_ui_view.py", line 299, in _inverse_arch
    view.write(data)
  File "/usr/src/app/odoo/addons/website/models/ir_ui_view.py", line 51, in write
    return super(View, self).write(vals)
  File "/usr/src/app/odoo/addons/base/models/ir_ui_view.py", line 490, in write
    return super(View, self).write(self._compute_defaults(vals))
  File "/usr/src/app/odoo/models.py", line 3546, in write
    real_recs._validate_fields(set(vals) - set(inverse_fields))
  File "/usr/src/app/odoo/models.py", line 1159, in _validate_fields
    check(self)
  File "/usr/src/app/odoo/addons/base/models/ir_ui_view.py", line 394, in _check_xml
    raise ValidationError("%s\n\n%s" % (_("Error while validating view"), tools.ustr(e)))
odoo.exceptions.ValidationError: ('Error while validating view\n\n沒有找到模型: bm.bug\n\n錯誤的上下文:\n視圖 `bug列表`\n[view_id: 567, xml_id: n/a, model: bm.bug, parent_id: n/a]', None)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/usr/src/app/odoo/http.py", line 619, in _handle_exception
    return super(JsonRequest, self)._handle_exception(exception)
  File "/usr/src/app/odoo/http.py", line 309, in _handle_exception
    raise pycompat.reraise(type(exception), exception, sys.exc_info()[2])
  File "/usr/src/app/odoo/tools/pycompat.py", line 14, in reraise
    raise value
  File "/usr/src/app/odoo/http.py", line 664, in dispatch
    result = self._call_function(**self.params)
  File "/usr/src/app/odoo/http.py", line 345, in _call_function
    return checked_call(self.db, *args, **kwargs)
  File "/usr/src/app/odoo/service/model.py", line 93, in wrapper
    return f(dbname, *args, **kwargs)
  File "/usr/src/app/odoo/http.py", line 338, in checked_call
    result = self.endpoint(*a, **kw)
  File "/usr/src/app/odoo/http.py", line 909, in __call__
    return self.method(*args, **kw)
  File "/usr/src/app/odoo/http.py", line 510, in response_wrap
    response = f(*args, **kw)
  File "/usr/src/app/odoo/addons/web/controllers/main.py", line 1323, in call_button
    action = self._call_kw(model, method, args, kwargs)
  File "/usr/src/app/odoo/addons/web/controllers/main.py", line 1311, in _call_kw
    return call_kw(request.env[model], method, args, kwargs)
  File "/usr/src/app/odoo/api.py", line 395, in call_kw
    result = _call_kw_multi(method, model, args, kwargs)
  File "/usr/src/app/odoo/api.py", line 382, in _call_kw_multi
    result = method(recs, *args, **kwargs)
  File "<decorator-gen-58>", line 2, in button_immediate_install
  File "/usr/src/app/odoo/addons/base/models/ir_module.py", line 72, in check_and_log
    return method(self, *args, **kwargs)
  File "/usr/src/app/odoo/addons/base/models/ir_module.py", line 463, in button_immediate_install
    return self._button_immediate_function(type(self).button_install)
  File "/usr/src/app/odoo/addons/base/models/ir_module.py", line 573, in _button_immediate_function
    modules.registry.Registry.new(self._cr.dbname, update_module=True)
  File "/usr/src/app/odoo/modules/registry.py", line 85, in new
    odoo.modules.load_modules(registry._db, force_demo, status, update_module)
  File "/usr/src/app/odoo/modules/loading.py", line 418, in load_modules
    processed_modules += load_marked_modules(cr, graph,
  File "/usr/src/app/odoo/modules/loading.py", line 310, in load_marked_modules
    loaded, processed = load_module_graph(
  File "/usr/src/app/odoo/modules/loading.py", line 222, in load_module_graph
    load_data(cr, idref, mode, kind='data', package=package, report=report)
  File "/usr/src/app/odoo/modules/loading.py", line 68, in load_data
    tools.convert_file(cr, package.name, filename, idref, mode, noupdate, kind, report)
  File "/usr/src/app/odoo/tools/convert.py", line 737, in convert_file
    convert_xml_import(cr, module, fp, idref, mode, noupdate, report)
  File "/usr/src/app/odoo/tools/convert.py", line 804, in convert_xml_import
    obj.parse(doc.getroot())
  File "/usr/src/app/odoo/tools/convert.py", line 716, in parse
    pycompat.reraise(
  File "/usr/src/app/odoo/tools/pycompat.py", line 13, in reraise
    raise value.with_traceback(tb)
  File "/usr/src/app/odoo/tools/convert.py", line 713, in parse
    self._tag_root(de)
  File "/usr/src/app/odoo/tools/convert.py", line 675, in _tag_root
    f(rec)
  File "/usr/src/app/odoo/tools/convert.py", line 675, in _tag_root
    f(rec)
  File "/usr/src/app/odoo/tools/convert.py", line 578, in _tag_record
    record = model._load_records([data], self.mode == 'update')
  File "/usr/src/app/odoo/models.py", line 4062, in _load_records
    records = self._load_records_create([data['values'] for data in to_create])
  File "/usr/src/app/odoo/addons/website/models/ir_ui_view.py", line 148, in _load_records_create
    records = super(View, self)._load_records_create(values)
  File "/usr/src/app/odoo/models.py", line 3976, in _load_records_create
    return self.create(values)
  File "<decorator-gen-31>", line 2, in create
  File "/usr/src/app/odoo/api.py", line 344, in _model_create_multi
    return create(self, arg)
  File "/usr/src/app/odoo/addons/base/models/ir_ui_view.py", line 473, in create
    return super(View, self).create(vals_list)
  File "<decorator-gen-3>", line 2, in create
  File "/usr/src/app/odoo/api.py", line 344, in _model_create_multi
    return create(self, arg)
  File "/usr/src/app/odoo/models.py", line 3757, in create
    fields[0].determine_inverse(batch_recs)
  File "/usr/src/app/odoo/fields.py", line 1096, in determine_inverse
    getattr(records, self.inverse)()
  File "/usr/src/app/odoo/addons/base/models/ir_ui_view.py", line 299, in _inverse_arch
    view.write(data)
  File "/usr/src/app/odoo/addons/website/models/ir_ui_view.py", line 51, in write
    return super(View, self).write(vals)
  File "/usr/src/app/odoo/addons/base/models/ir_ui_view.py", line 490, in write
    return super(View, self).write(self._compute_defaults(vals))
  File "/usr/src/app/odoo/models.py", line 3546, in write
    real_recs._validate_fields(set(vals) - set(inverse_fields))
  File "/usr/src/app/odoo/models.py", line 1159, in _validate_fields
    check(self)
  File "/usr/src/app/odoo/addons/base/models/ir_ui_view.py", line 394, in _check_xml
    raise ValidationError("%s\n\n%s" % (_("Error while validating view"), tools.ustr(e)))
odoo.tools.convert.ParseError: "Error while validating view

沒有找到模型: bm.bug

錯誤的上下文:
視圖 `bug列表`
```xml
[view_id: 567, xml_id: n/a, model: bm.bug, parent_id: n/a]
None" while parsing /mnt/extra-addons/bug-manage/views/bugs.xml:1, near
<odoo>
  <data>
    <!-- explicit list view definition -->
    <record model="ir.ui.view" id="bug-manage.list">
      <field name="name">bug列表</field>
      <field name="model">bm.bug</field>
      <field name="arch" type="xml">
        <tree>
          <field name="name"/>
          <field name="is_closed"/>
          <field name="user_id"/>
        </tree>
      </field>
    </record>
    <record model="ir.ui.view" id="bug-manage.form">
      <field name="name">bug表单</field>
      <field name="model">bm.bug</field>
      <field name="arch" type="xml">
        <form>
          <header>
              <button name="do_close" type="object" string="关闭bug"/>
          </header>
          <sheet>
              <group name="group_top" col="2">
                  <group name="group_left">
                      <field name="name"/>
                      <field name="user_id"/>
                      <field name="is_closed"/>
                  </group>
                  <group name="group_right">
                      <field name="close_reason"/>
                      <field name="follower_id"/>
                  </group>
              </group>
              <notebook>
                  <page string="详细内容">
                      <field name="detail"/>
                  </page>
              </notebook>
          </sheet>
        </form>
      </field>
    </record>
    <record model="ir.ui.view" id="bug-manage.search">
      <field name="name">bug搜索</field>
      <field name="model">bm.bug</field>
      <field name="arch" type="xml">
        <search>
          <field name="name"/>
          <field name="is_closed"/>
          <field name="user_id"/>
        </search>
      </field>
    </record>
    <!-- actions opening views on models -->
    <record model="ir.actions.act_window" id="bug-manage.action_window">
      <field name="name">bug-manage window</field>
      <field name="res_model">bm.bug</field>
      <field name="view_mode">tree,form</field>
    </record>

    <!-- Top menu item -->
    <menuitem name="bug管理系统" id="bug-manage.menu_root"/>

    <!-- menu categories -->
    <menuitem name="bug管理" id="bug-manage.menu_1" parent="bug-manage.menu_root"/>

    <!-- actions -->
    <menuitem name="bug列表" id="bug-manage.menu_1_list" parent="bug-manage.menu_1" action="bug-manage.action_window"/>
  </data>
</odoo>
```
錯誤:
Odoo Server Error
```log
Traceback (most recent call last):
  File "/usr/src/app/odoo/http.py", line 619, in _handle_exception
    return super(JsonRequest, self)._handle_exception(exception)
  File "/usr/src/app/odoo/http.py", line 309, in _handle_exception
    raise pycompat.reraise(type(exception), exception, sys.exc_info()[2])
  File "/usr/src/app/odoo/tools/pycompat.py", line 14, in reraise
    raise value
  File "/usr/src/app/odoo/http.py", line 664, in dispatch
    result = self._call_function(**self.params)
  File "/usr/src/app/odoo/http.py", line 345, in _call_function
    return checked_call(self.db, *args, **kwargs)
  File "/usr/src/app/odoo/service/model.py", line 93, in wrapper
    return f(dbname, *args, **kwargs)
  File "/usr/src/app/odoo/http.py", line 338, in checked_call
    result = self.endpoint(*a, **kw)
  File "/usr/src/app/odoo/http.py", line 909, in __call__
    return self.method(*args, **kw)
  File "/usr/src/app/odoo/http.py", line 510, in response_wrap
    response = f(*args, **kw)
  File "/usr/src/app/odoo/addons/web/controllers/main.py", line 1323, in call_button
    action = self._call_kw(model, method, args, kwargs)
  File "/usr/src/app/odoo/addons/web/controllers/main.py", line 1311, in _call_kw
    return call_kw(request.env[model], method, args, kwargs)
  File "/usr/src/app/odoo/api.py", line 395, in call_kw
    result = _call_kw_multi(method, model, args, kwargs)
  File "/usr/src/app/odoo/api.py", line 382, in _call_kw_multi
    result = method(recs, *args, **kwargs)
  File "<decorator-gen-58>", line 2, in button_immediate_install
  File "/usr/src/app/odoo/addons/base/models/ir_module.py", line 72, in check_and_log
    return method(self, *args, **kwargs)
  File "/usr/src/app/odoo/addons/base/models/ir_module.py", line 463, in button_immediate_install
    return self._button_immediate_function(type(self).button_install)
  File "/usr/src/app/odoo/addons/base/models/ir_module.py", line 573, in _button_immediate_function
    modules.registry.Registry.new(self._cr.dbname, update_module=True)
  File "/usr/src/app/odoo/modules/registry.py", line 85, in new
    odoo.modules.load_modules(registry._db, force_demo, status, update_module)
  File "/usr/src/app/odoo/modules/loading.py", line 418, in load_modules
    processed_modules += load_marked_modules(cr, graph,
  File "/usr/src/app/odoo/modules/loading.py", line 310, in load_marked_modules
    loaded, processed = load_module_graph(
  File "/usr/src/app/odoo/modules/loading.py", line 179, in load_module_graph
    load_openerp_module(package.name)
  File "/usr/src/app/odoo/modules/module.py", line 365, in load_openerp_module
    __import__('odoo.addons.' + module_name)
  File "/mnt/extra-addons/bug-manage/__init__.py", line 4, in <module>
    from . import models
  File "/mnt/extra-addons/bug-manage/models/__init__.py", line 4, in <module>
    from . import bugs
  File "/mnt/extra-addons/bug-manage/models/bugs.py", line 5, in <module>
    class Bug(models.Model):
  File "/mnt/extra-addons/bug-manage/models/bugs.py", line 15, in Bug
    @api.multi
AttributeError: module 'odoo.api' has no attribute 'multi'
```
