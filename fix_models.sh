#!/usr/bin/env bash
set -e

# models/user.py
cat > models/user.py << 'EOF'
#!/usr/bin/python3
"""User module: inherits from BaseModel."""
from models.base_model import BaseModel

class User(BaseModel):
    """User class: public class attributes."""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
EOF

# models/state.py
cat > models/state.py << 'EOF'
#!/usr/bin/python3
"""State module: inherits from BaseModel."""
from models.base_model import BaseModel

class State(BaseModel):
    """State class: public class attribute."""
    name = ""
EOF

# models/city.py
cat > models/city.py << 'EOF'
#!/usr/bin/python3
"""City module: inherits from BaseModel."""
from models.base_model import BaseModel

class City(BaseModel):
    """City class: public class attributes."""
    state_id = ""
    name = ""
EOF

# models/amenity.py
cat > models/amenity.py << 'EOF'
#!/usr/bin/python3
"""Amenity module: inherits from BaseModel."""
from models.base_model import BaseModel

class Amenity(BaseModel):
    """Amenity class: public class attribute."""
    name = ""
EOF

# models/place.py
cat > models/place.py << 'EOF'
#!/usr/bin/python3
"""Place module: inherits from BaseModel."""
from models.base_model import BaseModel

class Place(BaseModel):
    """Place class: public class attributes."""
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
EOF

# models/review.py
cat > models/review.py << 'EOF'
#!/usr/bin/python3
"""Review module: inherits from BaseModel."""
from models.base_model import BaseModel

class Review(BaseModel):
    """Review class: public class attributes."""
    place_id = ""
    user_id = ""
    text = ""
EOF

echo "✅ Model files have been fixed."

