function taskFor(id) {
  return "Read /root/LearnDutch/dataset/packs/" + id + ".json and /root/LearnDutch/dataset/frames.json. Write /root/LearnDutch/dataset/shards/" + id + ".json with exactly pack.n spoken sentences as a JSON array. Use only pack nouns/verbs/adjs plus function words from the phraser prompt. Honour pack tags, level, and noun article. audio null. Do not touch other shards. Write the file as soon as the sentences are ready.";
}

const ids = ["s01","s02","s03","s04","s05","s06","s07","s08","s09","s10","s11","s12","s13","s14","s15","s16","s17","s18","s19","s20","s21","s22","s23","s24"];
const all = [];
let i = 0;
while (i < ids.length) {
  const id = ids[i];
  const result = await runs.run(id, {
    agent: "phraser",
    task: taskFor(id),
    acceptance: false
  });
  all.push(result);
  i = i + 1;
}

const merge = await runs.run("merge", {
  agent: "worker",
  task: "In /root/LearnDutch run: python3 pipeline/merge.py && python3 pipeline/validate.py. If validate fails, fix the bad shard (not by inventing lemmas), rerun merge+validate. Do not write 1000 sentences yourself. Report counts.",
  acceptance: false
});
return { ok: merge.ok, n: all.length, output: merge.output };
