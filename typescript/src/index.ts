type Division =
  Array<{
    name: string,
    points: number,
  }>

export const getResults = (division: Division, n: number) => {

  let resultString = '';
  const sortedDivision = division.sort((a, b) => b.points - a.points);
  const promote = sortedDivision.slice(0, n);
  const relegate = sortedDivision.slice(sortedDivision.length - n, sortedDivision.length);

  // Check if teams are in both the top n and bottom n
  promote.forEach((p) => {
    const foundCommon = relegate.find(r => r.name === p.name);

    if (foundCommon) {
      resultString += `Team ${p.name} is in both promote and relegate catergories`;
      return;
    }
  });

  if (resultString.length > 0) {
    return resultString;
  }

  // Format and return the result.
  resultString += "Promote:\n";
  promote.map(p => resultString += p.name + "\n");

  resultString += "\n";

  resultString += "Relegate:\n";
  relegate.map(r => resultString += r.name + "\n");

  return resultString.slice(0, resultString.length - 1);
};
