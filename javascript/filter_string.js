const filterString = (str, char) = {
  let i = 0;
  const end = str.length - 1;
  while (i <= end) {
    if (str[i] === char) {
      str[i] = ' ';
    }
  }
  return str;
}
