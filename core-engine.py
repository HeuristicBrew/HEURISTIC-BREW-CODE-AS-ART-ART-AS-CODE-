
import random
import uuid
from core.templates import BASELINE_MANIFESTO

class UltimateObserverEngine:
    """
    Non-custodial variant engine. Stores no state outside the local runtime memory map.
    Approaching reality through a series of recursive updates.
    """
    def __init__(self):
        self.instance_id = uuid.uuid4().hex[:8]
        self.entropy_rate = 0.044
        self.history = [BASELINE_MANIFESTO]

    def strip_metadata_labels(self, data_stream):
        """The Well Dressed Girl script: Rips external classification tags."""
        return data_stream.strip().replace("[CLASSIFIED]", "").replace("[TARGET]", "")

    def inject_stochastic_resonance(self, text_stream):
        """Cranium Space Funk: Implements noise injection to preserve fluidity."""
        chars = list(text_stream)
        if random.random() < 0.33:
            idx = random.randint(0, len(chars) - 1)
            chars[idx] = random.choice(['~', '_', '(a)', '•', '*'])
        return "".join(chars)

    def spawn_unique_variant(self, source_text):
        """Generates an organic, community-ready copy of a copy."""
        clean = self.strip_metadata_labels(source_text)
        noisy = self.inject_stochastic_resonance(clean)
        
        words = noisy.split()
        mutated_words = []
        
        for word in words:
            if random.random() < self.entropy_rate:
                mutated_words.append(word)
                mutated_words.append(word)
            elif random.random() < (self.entropy_rate / 2):
                continue
            else:
                mutated_words.append(word)
                
        variant = " ".join(mutated_words)
        self.history.append(variant)
        return variant
