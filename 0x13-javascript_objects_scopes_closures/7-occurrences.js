#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  const nb = list.filter((element) => element === searchElement).length;
  return nb;
};
