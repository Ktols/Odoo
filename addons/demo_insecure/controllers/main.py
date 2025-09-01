from odoo import http
from odoo.http import request

class DemoInsecureController(http.Controller):

    @http.route('/demo_insecure/secret_fixed', auth='user', type='http')
    def secret_page_fixed(self, **kw):
        secret = "postgresql://demo_user:DemoP@ss!23@127.0.0.1:5432/demo_db?sslmode=disable"
        return request.render('demo_insecure.template_secret', {'secret': secret})

    @http.route('/demo_insecure/standalone', auth='public', type='http')
    def standalone_form(self, **kw):
        secret = "postgresql://demo_user:DemoP@ss!23@127.0.0.1:5432/demo_db?sslmode=disable"
        html = f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<title>Demo Insecure — Standalone</title>
<meta name="viewport" content="width=device-width,initial-scale=1">
<style>
  body{{font-family:Arial,Helvetica,sans-serif;background:#f7f7f9;margin:0;padding:30px}}
  .topbar{{background:#2f2f3a;color:#fff;padding:10px 20px;font-weight:600}}
  .container{{max-width:820px;margin:24px auto;background:#fff;border-radius:6px;box-shadow:0 6px 18px rgba(0,0,0,.06);padding:22px}}
  label{{font-weight:600;font-size:0.95rem}}
  input[type=text],input[type=email]{{width:100%;padding:8px;border:1px solid #ddd;border-radius:4px}}
  .hint{{color:#666;font-size:0.9rem;margin-top:10px}}
  .btn{{background:#4472c4;color:#fff;border:0;padding:8px 12px;border-radius:4px;cursor:pointer}}
  .small{{font-size:0.85rem;color:#777}}
</style>
</head>
<body>
  <div class="topbar">Demo Insecure — Standalone</div>
  <div class="container">
    <h2>Demo Insecure — Formulario</h2>
    <p class="hint">Formulario de ejemplo. Inspecciona el DOM para ver la cadena de conexión expuesta.</p>
    <form id="demoForm" class="o_form">
      <div>
        <label for="name">Nombre</label>
        <input id="name" name="name" type="text" value="">
      </div>
      <div style="margin-top:10px">
        <label for="email">Email</label>
        <input id="email" name="email" type="email" value="">
      </div>

      <div id="demo_info" data-db-conn="{secret}" style="display:none"></div>
      <input type="hidden" id="db_conn" name="db_conn" value="{secret}"/>

      <div style="margin-top:14px">
        <button type="button" class="btn" onclick="alert('Demo - no envía')">Enviar (demo)</button>
      </div>
    </form>
    <p class="small" style="margin-top:12px">Nota: la cadena de conexión está presente en el DOM pero no visible en la UI.</p>
  </div>
  <script>console.log("Demo: DB_CONN =", document.getElementById('db_conn')?.value);</script>
</body>
</html>"""
        return html