function cleanSet(set, startString) {
  if (!(set instanceof Set)) {
    throw new Error("The argument must be a Set");
  }
  if (!(startString instanceof String)) {
    return ("");
  }

  const tab = [...set]
    .filter((value) => value.startsWith(startString))
    .map((value) => value.slice(startString.length))
    .join('-');

  return tab;
}
