from typing import Dict, Any, Optional
from processing.utils import normal_generator

def main(event: Dict[Any, Any], context: Optional[Dict[Any, Any]] = None) -> None:
    normal_data = normal_generator(100, 5, 1)
    print(normal_data)

if __name__ == "__main__":
    main({None: None})