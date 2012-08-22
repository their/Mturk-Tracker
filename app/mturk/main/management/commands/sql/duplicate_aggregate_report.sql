CREATE OR REPLACE FUNCTION count_extra(
    istart TIMESTAMP WITH TIME ZONE, iend TIMESTAMP WITH TIME ZONE)
        RETURNS VOID AS '
    DECLARE
        total_hmv integer; corrected_hmv integer;
        removed_hmv integer; extra_avg_hmv float;
        correct_hmv integer;
        total_hgs integer; corrected_hgs integer;
        removed_hgs integer; extra_avg_hgs float;
        bad_crawl_hgs_count integer;
        correct_hgs integer;
    BEGIN
        RAISE NOTICE ''Counting multiplied records in main_hitgroupstatus
        and hits_mv tables.'';
        RAISE NOTICE ''Interval: % to %'', istart, iend;
        SELECT count(*)
        INTO total_hgs
        FROM main_hitgroupstatus
        WHERE crawl_id > (
                    SELECT min(id) FROM main_crawl
                    WHERE start_time BETWEEN istart AND iend
                ) AND
                crawl_id < (
                    SELECT max(id) FROM main_crawl
                    WHERE start_time BETWEEN istart AND iend
                );

        SELECT INTO
            corrected_hgs, removed_hgs, extra_avg_hgs *
        FROM (
            SELECT count(*), sum(asd.extra - 1), avg(asd.extra - 1)
            FROM (
                SELECT group_id, crawl_id, count(*) AS extra
                FROM main_hitgroupstatus
                WHERE
                    crawl_id > (
                        SELECT min(id) FROM main_crawl
                        WHERE start_time BETWEEN istart AND iend
                    ) AND
                    crawl_id < (
                        SELECT max(id) FROM main_crawl
                        WHERE start_time BETWEEN istart AND iend
                    )
                GROUP BY crawl_id, group_id
                HAVING count(*) > 1
            ) as asd
        ) as zxc;

        SELECT
            count(*)
        INTO
            bad_crawl_hgs_count
        FROM
            main_hitgroupstatus
        WHERE
            crawl_id IN (
                SELECT id FROM main_crawl
                WHERE
                    groups_available * 0.9 > groups_downloaded AND
                    start_time BETWEEN istart AND iend
            );
        correct_hgs = total_hgs - coalesce(removed_hgs, 0) -
                      coalesce(bad_crawl_hgs_count, 0);
        RAISE NOTICE ''main_hitgroupstatus table'';
        RAISE NOTICE ''Total:      %'', total_hgs;
        RAISE NOTICE ''Bad crawls: %'', bad_crawl_hgs_count;
        RAISE NOTICE ''Correct:    %'', correct_hgs;
        RAISE NOTICE ''To correct:  %'', corrected_hgs;
        RAISE NOTICE ''To remove:   %'', coalesce(removed_hgs, 0);
        RAISE NOTICE ''Extra avg:   %'', coalesce(extra_avg_hgs, 0);

        SELECT count(*)
        INTO total_hmv
        FROM hits_mv
        WHERE crawl_id > (
                    SELECT min(id) FROM main_crawl
                    WHERE start_time BETWEEN istart AND iend
                ) AND
                crawl_id < (
                    SELECT max(id) FROM main_crawl
                    WHERE start_time BETWEEN istart AND iend
                );

        SELECT INTO
            corrected_hmv, removed_hmv, extra_avg_hmv *
        FROM (
            SELECT count(*), sum(asd.extra - 1), avg(asd.extra - 1)
            FROM (
                SELECT group_id, crawl_id, count(*) AS extra
                FROM hits_mv
                WHERE
                    crawl_id > (
                        SELECT min(id) FROM main_crawl
                        WHERE start_time BETWEEN istart AND iend
                    ) AND
                    crawl_id < (
                        SELECT max(id) FROM main_crawl
                        WHERE start_time BETWEEN istart AND iend
                    )
                GROUP BY crawl_id, group_id
                HAVING count(*) > 1
            ) as asd
        ) as zxc;

        correct_hmv = total_hmv - coalesce(removed_hmv, 0);

        RAISE NOTICE ''hits_mv table'';
        RAISE NOTICE ''Total:      %'', total_hmv;
        RAISE NOTICE ''Correct:    %'', correct_hmv;
        RAISE NOTICE ''To correct: %'', corrected_hmv;
        RAISE NOTICE ''To remove:  %'', coalesce(removed_hmv, 0);
        RAISE NOTICE ''Extra avg:  %'', coalesce(extra_avg_hmv, 0);

        if (correct_hmv = correct_hgs) then
            RAISE NOTICE ''OK! correct_hmv == correct_hgs'';
        else
            RAISE NOTICE ''ERROR! correct_hmv != correct_hgs'';
        end if;
    END;
'
LANGUAGE plpgsql;