const createPushNotificationsJobs = (jobs, queue) => {
  if (!(jobs instanceof Array)) throw Error("Jobs is not an array");
    jobs.forEach((j) => {
    const job = queue.create("push_notification_code_3", j).save((err) => {
    if (!err) console.log(`Notification job created: ${job.id}`);
    });
    job.on("complete", () =>
    console.log(`Notification job ${job.id} completed`)
    );
    job.on("failed", (error) =>
    console.log(`Notification job ${job.id} failed: ${error}`)
    );
    job.on("progress", (progress) =>
    console.log(`Notification job ${job.id} ${progress}% complete`)
    );
  });
};

module.exports = createPushNotificationsJobs;
