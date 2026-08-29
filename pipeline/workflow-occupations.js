function taskFor(id) {
  return "Read /root/LearnDutch/dataset/occ_packs/" + id + ".json. Write /root/LearnDutch/dataset/occ_shards/" + id + ".json with exactly pack.n occupation objects as a JSON array. Use only pack tags. English labels, EN+ES aliases. Do not invent Dutch sentence words. Do not touch other shards.";
}

const ids = ["o01","o02","o03","o04","o05","o06","o07","o08","o09","o10"];
const all = [];
let i = 0;
while (i < ids.length) {
  const id = ids[i];
  const result = await runs.run(id, {
    agent: "jobs",
    task: taskFor(id),
    acceptance: false
  });
  all.push(result);
  i = i + 1;
}

const merge = await runs.run("merge", {
  agent: "worker",
  task: "In /root/LearnDutch run: python3 pipeline/merge_occupations.py. If it fails, fix the bad occ shard (do not invent a whole new list yourself), rerun. Report the count. Do not write occupations.json from scratch.",
  acceptance: false
});
return { ok: merge.ok, n: all.length, output: merge.output };
