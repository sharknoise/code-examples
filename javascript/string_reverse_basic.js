const reverse1 = (str) => {
  let i = 0;
  let result = '';
  while (i < str.length) {
    result = `${str[i]}${result}`;
    i = i + 1;
  }

  return result;
};

const reverse2 = (str) => {
  let i = str.length - 1;
  let result = '';
  while (i >= 0) {
    result = `${result}${str[i]}`;
    i = i - 1;
  }

  return result;
};
