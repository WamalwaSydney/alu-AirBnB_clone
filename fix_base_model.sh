#!/usr/bin/env bash
set -e

cat > models/base_model.py << 'EOF'
#!/usr/bin/python3
"""BaseModel module: defines all common attributes/methods."""
import uuid
from datetime import datetime

class BaseModel:
    """BaseModel defines id, created_at, updated_at and serialization."""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel instance."""
        if kwargs:
            for key, value in kwargs.items():
                if key in ('created_at', 'updated_at'):
                    setattr(self, key, datetime.fromisoformat(value))
                elif key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            # import storage here to avoid circular import at module load
            from models import storage
            storage.new(self)

    def __str__(self):
        """Return string representation."""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__
        )

    def save(self):
        """Update updated_at and save to file."""
        self.updated_at = datetime.now()
        # import storage here to avoid circular import at module load
        from models import storage
        storage.save()

    def to_dict(self):
        """Return dict of instance for JSON serialization."""
        d = self.__dict__.copy()
        d['__class__'] = self.__class__.__name__
        d['created_at'] = self.created_at.isoformat()
        d['updated_at'] = self.updated_at.isoformat()
        return d
EOF

echo "✅ models/base_model.py has been rewritten to avoid circular imports."

