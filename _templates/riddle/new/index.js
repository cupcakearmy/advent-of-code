const { default: axios } = require('axios')

async function getInput(year, day) {
  const { data } = await axios({
    url: `https://adventofcode.com/${year}/day/${day}/input`,
    headers: {
      Cookie: `session=${process.env.TOKEN};`,
    },
  })
  return data
}

module.exports = {
  params: async ({ args }) => {
    const day = args.day.toString().padStart(2, '0') // Padded
    return {
      ...args,
      id: `${args.year}-${day}`,
      dir: `./${args.year}/${day}`,
      input: await getInput(args.year, parseInt(day)),
      day,
    }
  },
}
