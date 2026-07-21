"""
SPACE AI 2.0

System Settings
"""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# ============================================
# DATABASE
# ============================================

DATA_DIR = BASE_DIR / "data"

DATABASE_FILE = DATA_DIR / "spaceman.db"

BACKUP_DIR = DATA_DIR / "backup"

# ============================================
# LOGS
# ============================================

LOG_DIR = BASE_DIR / "logs"

# ============================================
# APPLICATION
# ============================================

DEBUG = True

AUTO_LEARNING = True

AUTO_BACKUP = True

AUTO_PRUNE_DATABASE = True

# ============================================
# DASHBOARD
# ============================================

REFRESH_INTERVAL = 3

GRAPH_POINTS = 500

# ============================================
# VERSION
# ============================================

APP_NAME = "Space AI"

VERSION = "2.0.0-alpha1"
