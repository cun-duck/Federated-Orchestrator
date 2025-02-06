# context_analyzer.py
import geocoder

def load_model_based_on_location(lat, lon):
    location_type = get_industrial_context(lat, lon)  # e.g "mining", "office"
    return ort.InferenceSession(f"Model_Zoo/{location_type}.onnx")
