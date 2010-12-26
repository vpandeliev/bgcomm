BEGIN;
ALTER TABLE "posts_page" ADD COLUMN "hide" boolean NOT NULL DEFAULT 0;
ALTER TABLE "posts_post" ADD COLUMN "hide" boolean NOT NULL DEFAULT 0;
ALTER TABLE "posts_event" ADD COLUMN "hide" boolean NOT NULL DEFAULT 0;
ALTER TABLE "posts_member" ADD COLUMN "paid" boolean NOT NULL DEFAULT 0;
COMMIT;