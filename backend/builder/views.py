# builder/views.py

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings
import json

@login_required
def dashboard(request):
    """
    This view serves our Vue.js application.
    
    It intelligently handles both DEVELOPMENT and PRODUCTION modes.
    """
    
    # --- The Fix is Here: Environment-Aware Logic ---
    
    # In DEVELOPMENT mode (DEBUG=True), we will point directly to the
    # Vite development server.
    if settings.DEBUG:
        context = {
            'is_debug': True,
            'vite_dev_server_url': 'http://localhost:5173' # The default Vite dev server URL
        }
    
    # In PRODUCTION mode (DEBUG=False), we will read the manifest file
    # that is created by the `npm run build` command.
    else:
        manifest_path = settings.BASE_DIR / 'static' / 'vite' / '.vite' / 'manifest.json'
        
        try:
            with open(manifest_path, 'r') as f:
                manifest = json.load(f)
        except FileNotFoundError:
            # A fallback in case the manifest is missing in production
            manifest = { 'src/main.ts': {'file': '', 'css': []} }

        entry = manifest.get('src/main.ts', {})

        context = {
            'is_debug': False,
            'vite_js_file': entry.get('file', ''),
            'vite_css_files': entry.get('css', [])
        }
    
    return render(request, 'builder/editor_entry.html', context)