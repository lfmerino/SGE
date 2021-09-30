
# -*- coding: utf-8 -*-

from odoo import models, fields, api

class mimenu(models.Model):
	_name = 'mimenu.test'
	name = field,Char('Nombre')
	stree = fields.Char('Calle')
#	value2 = fields.Float(compute="_value_pc", stor=True)
#	description = field.Text()
#
#	@api.depends('value')
#	def _value_pc(self):
#		self.value2 = float(self/value) / 100


view
<odoo>
	<data>
		<record id="mimenu_test_tree" model="ir.ui.view">
			<field name="name"> mimenu.data.test.tree</field>
			<field name="model">mimenu.test</field>
			<field name="arch" type="xml"> 
		</record>

	</data>
</odoo>




<odoo>
	<data>
		<!-- explicit list view definition -->
		<!--
		<record model="ir.ui.view" id="zaxeboa.list"
			<field name="name">zaxeboa list</field>
			<field name="model">zaxeboa.zaxeboa</field>
			<field name="arch"type="xml>
				<tree>
					<field name="name"/>
					<field name="value"/>
					<field name="value2"/>
				</tree>
			</field>
		</record>
		-->

		<!-- actions opening views on models -->
		<!--
		<record model="ir.actions.act_windows" id="zaxeboa.action_window"
			<field name="name">zaxeboa windowt</field>
			<field name="res_model">zaxeboa.zaxeboa</field>
			<field name="view_mode">tree,form</field>
		</record>
		-->

		<!-- server action to the one above -->
		<!--
		<record model="ir.actions.server" id="zaxeboa.action_server"
			<field name="name">zaxeboa server</field>
			<field name="model_id" ref=model_zaxeboa_zaxeboa/>
			<field name="state"code </field>
			<field name="code">
				action = {
					"tyoe": "ir.actions.act_windows",
					"view_mode": "tree,form",
					res_model: self._name,
			</field>
		</record>
		-->


<odoo>
	<data>
		<!-- explicit list view definition -->
		<record model="ir.ui.view" id="zaxeboa.zaxeboa_list"
			<field name="name">Lista de empresast</field>
			<field name="model">res.partner</field>
			<field name="arch"type="xml>
				<tree>
					<field name="id"/>
					<field name="name"/>
					<field name="title"/>
					<field name="credit_limit"/>
					<field name="street"/>
					<field name="zip"/>
					<field name="city"/>
					<field name="phone"/>
				</tree>
			</field>
		</record>


		<!-- actions opening views on models -->
		<record model="ir.actions.act_window" id="zaxeboa.action__zaxeboa_window"
			<field name="name">zaxeboa windowt</field>
			<field name="res_model">res.partner</field>
			<field name="view_mode">tree,form</field>
		</record>

		<!-- Top menu item -->
		<menuitem name="Zaxeboa" id="zaxeboa.menu_root"/>
		<!-- Top menu item -->
		<menuitem name="Mantenimiento" id="zaxeboa.menu_1" parent="zaxeboa.menu_root"/>
		<!-- Top menu item -->
		<menuitem name="Zaxeboa" id="zaxeboa.menu_zaxeboz_list" parent="zaxeboa_menu_1
			action = "zaxeboa.action_zaxeboa_windows"/>	
	</daata
</odoo>





