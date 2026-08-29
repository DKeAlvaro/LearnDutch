function taskFor(id) {
  return "Read /root/LearnDutch/dataset/frame_packs/" + id + ".json and /root/LearnDutch/dataset/glue.json. Write /root/LearnDutch/dataset/frame_shards/" + id + ".json with exactly pack.n frames as a JSON array. Literals only from glue.json. Slots only from the pack. Spoken Dutch. Do not touch other shards.";
}

const ids = ["f01","f02","f03","f04","f05","f06","f07","f08","f09","f10","f11","f12"];
const all = [];
let i = 0;
while (i < ids.length) {
  const id = ids[i];
  const result = await runs.run(id, {
    agent: "framer",
    task: taskFor(id),
    acceptance: false
  });
  all.push(result);
  i = i + 1;
}

const merge = await runs.run("merge", {
  agent: "worker",
  task: "In /root/LearnDutch run: python3 pipeline/merge_frames.py. If it fails, fix the bad frame shard (literals must be in glue.json), rerun. Report the count. Do not write frames.json from scratch.",
  acceptance: false
});
return { ok: merge.ok, n: all.length, output: merge.output };
