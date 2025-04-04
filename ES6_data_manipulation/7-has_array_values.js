export default function hasValuesFromArray(set, array) {
  if (!(set instanceof Set)) {
    throw new Error("The argument must be a Set");
  }
  if (!Array.isArray(array)) {
    return [];
  }
  return array.every((element) => set.has(element));
}
