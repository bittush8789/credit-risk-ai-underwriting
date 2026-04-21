import joblib
import os
import logging

logger = logging.getLogger("CreditRiskAPI")

# Define paths to model artifacts
MODEL_DIR = os.path.join(os.path.dirname(__file__), "..", "models")

class ModelLoader:
    def __init__(self):
        self.model = None
        self.scaler = None
        self.encoder = None
        self.meta = None

    def load_v4_engine(self):
        """Loads the enterprise-grade V4 underwriting engine."""
        try:
            self.model = joblib.load(os.path.join(MODEL_DIR, "best_underwriting_model.pkl"))
            self.scaler = joblib.load(os.path.join(MODEL_DIR, "scaler.pkl"))
            self.encoder = joblib.load(os.path.join(MODEL_DIR, "encoder.pkl"))
            self.meta = joblib.load(os.path.join(MODEL_DIR, "v4_meta.pkl"))
            logger.info("V4 Underwriting Engine loaded successfully.")
        except Exception as e:
            logger.error(f"Failed to load V4 engine: {e}")
            raise

# Singleton instance
engine = ModelLoader()
engine.load_v4_engine()
