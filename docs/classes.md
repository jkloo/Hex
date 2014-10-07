# Classes

## Tile Scope

### `Tile`

```python
class Tile(Widget):
    location = (x, y)  # location on grid
    ...
```

Subclassing Tile:
```python
class GrassTile(Tile):
    _sources = []  # image sources.
    _entry = {'U': True, 'D': True, 'L': True, 'R': True}
    ...
```

### `Character`

```python
class Character(Widget):
    location = (x, y)  # location on grid
    ...
```

```python
class PlayerCharacter(Character):
    _animate = {'U': [], 'D': [], 'L': [], 'R': []}  # animations for character
    ...
```

```python
class NonPlayerCharacter(Character):
    _animate = {'U': [], 'D': [], 'L': [], 'R': []}  # animations for character
    ...
```

### `SingleObject`
```python
class SingleObject(Widget):
    location = (x, y)  # location on grid
    _actions = {'U': None, 'D': None, 'L': None, 'R': None}  # action handlers. local (x, y, direction)
    ...
```

```python
class TreeObject(SingleObject):
    _entry = {'U': False, 'D': False, 'L': False, 'R': False}
    _sources = []  # image sources
    ...
```

```python
class BushObject(SingleObject):
    _entry = {'U': True, 'D': True, 'L': True, 'R': True}
    _sources = []  # image sources
    ...
```

### `MultiObject`
```python
class MultiObject(Widget):
    location = (x, y)  # root location on grid
    size = (w, h)  # number of tiles occupied
    _sources = []  # image sources (either single image, or w * h images)
    _objects = []  # list of Objects
```

    - `BuildingObject`
        - (BuildingTypes ...)
    - `PickupObject`
        - (PickupTypes ...)

## World Scope

- `Grid`
- `Region`
- `World`
