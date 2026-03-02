# eureka.py
import logging
import py_eureka_client.eureka_client as eureka_client

logger = logging.getLogger(__name__)

# ==========================
# Configuration Eureka
# ==========================
EUREKA_SERVER = "http://192.168.11.192:8761/eureka/"
APP_NAME = "stock-service"
INSTANCE_PORT = 8000
INSTANCE_HOST = "192.168.11.139"

# ==========================
# Initialisation du client Eureka
# ==========================
def start_eureka():
    try:
        eureka_client.init(
            eureka_server=EUREKA_SERVER,
            app_name=APP_NAME,
            instance_port=INSTANCE_PORT,
            instance_host=INSTANCE_HOST,
            renewal_interval_in_secs=30,
            duration_in_secs=90
        )
        logger.info(f"[Eureka] {APP_NAME} enregistré avec succès sur {EUREKA_SERVER}")
    except Exception as e:
        logger.error(f"[Eureka] Impossible de s'enregistrer sur Eureka : {e}")

# Lancer le client Eureka dès l'import
start_eureka()