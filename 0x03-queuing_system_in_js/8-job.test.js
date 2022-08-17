import kue from "kue";
import { expect } from "chai";
import createPushNotificationsJobs from "./8-job";

const queue = kue.createQueue();

describe("createPushNotificationsJobs", () => {
  before(() => {
    queue.testMode.enter();
  });

  afterEach(() => {
    queue.testMode.clear();
  });

  after(() => {
    queue.testMode.exit();
  });

  it("if jobs is not an array passing Number", () => {
    expect(() => {
      createPushNotificationsJobs(2, queue);
    }).to.throw("Jobs is not an array");
  });

  it("if jobs is not an array passing Object", () => {
    expect(() => {
      createPushNotificationsJobs({}, queue);
    }).to.throw("Jobs is not an array");
  });

  it("if jobs is not an array passing String", () => {
    expect(() => {
      createPushNotificationsJobs("Hello", queue);
    }).to.throw("Jobs is not an array");
  });
});
