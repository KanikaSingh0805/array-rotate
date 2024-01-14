def rotate_array(arr, steps, direction="left"):
  """Rotates the elements of an array to the left or right by a given number of steps.

  Args:
    arr: The array to be rotated.
    steps: The number of steps to rotate the array (positive for left, negative for right).
    direction: The direction of rotation ("left" or "right").

  Returns:
    The rotated array.
  """

  if not isinstance(arr, list):
    raise TypeError("Input must be a list.")

  if not isinstance(steps, int):
    raise TypeError("Number of steps must be an integer.")

  if direction not in ("left", "right"):
    raise ValueError("Invalid rotation direction.")

  n = len(arr)
  steps %= n  # Handle steps exceeding array length

  if direction == "left":
    return arr[steps:] + arr[:steps]  # Slice and concatenate for left rotation
  else:
    return arr[-steps:] + arr[:-steps]  # Slice and concatenate for right rotation
