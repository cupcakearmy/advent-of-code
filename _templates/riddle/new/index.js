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
    return { ...args, input: await getInput(args.year, args.day) }
  },
}
