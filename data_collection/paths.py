from pathlib import Path


MODULE_DIR = Path(__file__).parent
MAIN_DIR = MODULE_DIR.parent
ASSETS_DIR = MAIN_DIR / "assets"

CUSTOM_COMPONENTS_DIR = ASSETS_DIR / "custom_components"
FOOTER_COMPONENTS_DIR = CUSTOM_COMPONENTS_DIR / "footer"

COMPANY_LOGO_ICO_PATH = ASSETS_DIR / "favicon.ico"
COMPANY_LOGO_PATH = ASSETS_DIR / "logo.jpg"
COMPANY_LOGO_FULL_PATH = COMPANY_LOGO_PATH.resolve()

