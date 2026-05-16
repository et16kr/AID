# S004 Tech Platform Disk IO

Date: 2026-05-16

Workspace: `/home/et16/AID`

## Requirement And Boundary

S004 performs a semantic-unit audit for disk I/O volume layout and Solaris, HPUX, AIX, and Linux platform setup technical documents.

Scoped Korean sources and English targets:

- `DOCK/Home/21. Altibase 디스크I_O 병목을 고려한 볼륨구성 가이드__11698408.md` -> `arch/Home/Configuration Guide For Minimizing Disk I_O Contention__22643018.md`
- `DOCK/Home/22. Altibase 운영을 위한 Solaris 설정 가이드__11698415.md` -> `arch/Home/Solaris Setup Guide for Altibase__14058290.md`; `arch/Home/Solaris Setup Guide for Altibase/1. Kernel Parameters__22643040.md`; `arch/Home/Solaris Setup Guide for Altibase/2. User Settings__14058294.md`; `arch/Home/Solaris Setup Guide for Altibase/3. Summary__14058296.md`
- `DOCK/Home/23. Altibase 운영을 위한 HPUX 설정 가이드__14057733.md` -> `arch/Home/HPUX Setup Guide for Altibase__14058288.md`
- `DOCK/Home/24. Altibase 운영을 위한 AIX 설정 가이드__13436846.md` -> `arch/Home/AIX Setup Guide for Altibase__14058298.md`
- `DOCK/Home/57. Altibase 운영을 위한 Linux 설정 가이드__13436485.md` -> `arch/Home/Linux Setup Guide for Altibase__22643022.md`

This job does not run the `llm-reference` consolidation workflow, does not edit Korean source documents, and does not delete or move English source documents. No English source document changes were required after direct comparison, so `manifest.json` metadata was not changed.

## Required Reading

Reviewed before editing:

- `AGENTS.md`
- `KO_EN_DOC_REVIEW_REPORT.md`
- `PASS2_KO_EN_DOC_REVIEW_REPORT.md`
- `LLM_REFERENCE_REVIEW_PLAN.md`
- `.codex-jobs/ko-en-semantic-coverage-audit/workflow-requirements.md`
- `.codex-jobs/ko-en-semantic-coverage-audit/prompts/S004.md`
- `semantic-coverage/README.md`
- `semantic-coverage/doc-mapping.tsv`
- The five Korean source documents and eight English target documents listed above

Previous J/P workflow reports were used only as orientation. Coverage decisions in `semantic-coverage/matrices/S004-tech-platform-disk-io.tsv` are based on direct inspection of the scoped Korean and English files.

## Pre-Edit State

- Branch: `combine`
- `git status --short` showed only `.codex-jobs/ko-en-semantic-coverage-audit/jobs.tsv` modified from `S004 ToDo` to `S004 Progress`.
- `git status --short --untracked-files=all -- . ':(exclude).codex-jobs' ':(exclude).codex-jobs/**'` produced no output, so there were no uncommitted project files outside the workflow area before S004 edits.
- S004 owns the full audit for the five scoped Korean technical documents.

## Design Note

S004 adds the semantic matrix and per-job note for the platform/disk I/O group:

- `semantic-coverage/matrices/S004-tech-platform-disk-io.tsv`
- `semantic-coverage/notes/S004-tech-platform-disk-io.md`

The product documentation structure is unchanged. The matrix records semantic units by topic section, compact table group, command/procedure block, warning, external reference, and attachment. Long OS command sections are summarized as one procedural semantic unit when the section has one operational purpose; exact commands, parameter names, paths, version numbers, and output identifiers are preserved in the matrix evidence.

Export metadata, Confluence TOCs, contact-only support boilerplate, and legal/warranty boilerplate are recorded as `not_applicable` because they do not change the technical platform setup baseline. Technical external references and URL-backed document-format attachments are still recorded and verified.

## Audit Summary

### D021 Disk I/O Volume Configuration

The English disk I/O guide covers the Korean source semantics for:

- WAL redo-log/data persistence and the Altibase `6.5 or later` basis
- redo log `mmap`/`LogSyncThread` behavior and the power/OS hang caveat
- memory DB checkpoint behavior, 32K memory pages, dirty pages, and separate redo/data disks
- disk DB buffer behavior, 8K pages, Flush List, LRU, and BufferReplace
- undo tablespace out-place versus in-place update semantics, MVCC, and recovery copy-back
- configuration examples for full separation, minimum separation, and complex/simple disk DB workload separation
- supported and unsupported file systems, including Direct I/O mount/property implications
- raw device and NFS/NAS limitations
- dedicated database storage, RAID 10, SSD recommendation for random I/O, file-cache/swap tuning, and OS platform cross-references
- Direct I/O properties `DIRECT_IO_ENABLED`, `DATABASE_IO_TYPE`, and `LOG_IO_TYPE`
- Direct I/O required actions by OS/file system, when Direct I/O is useful, when Buffered I/O is useful, and fixed Altibase page sizes
- all three Korean-source PDF attachment links

### D022 Solaris Setup

The split English Solaris guide covers the Korean source semantics for:

- Solaris setup purpose, `altibase.properties` reference, Altibase `v6 or later`, and Sun OS `5.8 ~ 5.10`
- shared memory concepts, `STARTUP_SHM_CHUNK_SIZE`, `EXPAND_CHUNK_PAGE_COUNT * 32K`, `shmmax`, `shmmni`, and `shmseg`
- semaphore synchronization concepts and rows for `semmns`, `semmni`, `semmsl`, `semmap`, `semmnu`, `semopm`, `semume`, and `semvmx`
- Solaris `5.10 or below` `/etc/system` settings
- Solaris `5.10 or later` `projadd`/`projmod` settings, `max-shm-memory` caution, and `projadd -l` check
- user resource limits, hard/soft limit behavior, and Solaris system-file options
- required environment variables, `LD_LIBRARY_PATH_64`, Altibase `5.3` character-set behavior, `ALTIBASE_NLS_USE`, and terminal font guidance
- summary kernel table and shell environment/resource example

### D023 HPUX Setup

The English HPUX guide covers the Korean source semantics for:

- HPUX setup purpose and Altibase Configuration File Guide reference
- shared memory and semaphore IPC concepts, parameter rows, and `IPC_CHANNEL_COUNT`
- file cache rationale, `dbc_min_pct`, `dbc_max_pct`, `filecache_min`, `filecache_max`, and HPUX `11.31` rename
- HP physical-memory threshold recommendation for `dbc_max_pct`
- resource-limit kernel rows, `maxdsiz_64bit`, `max_thread_proc`, `maxfiles`, `nproc`, and HPUX `11.23` `maxusers` condition
- `kmtune`, `kctune`, `sam`, root/reboot guidance, and all shared-memory, semaphore, file-cache, and resource-limit command examples
- user resource limits, open-files capacity factors, hard/soft limits, and HPUX `sam`/`kctune` handling
- required environment variables, `SHLIB_PATH`, HPUX multithread variables, `PTHREAD_FORCE_SCOPE_SYSTEM`, `PERF_ENABLE`, `PTHREAD_FAST_SHARED_OBJECTS`, and `PTHREAD_DISABLE_HANDOFF`
- `_M_ARENA_OPTS` tuning ranges, example, fragmentation risk, and low-memory `1:8` case
- pthread cumulative patch check with `swlist -l patch | grep pthread`
- `PHCO_33675`/`PHCO_34718` and `PTHREAD_SHARED_MUTEX_OLDSPIN`
- summary kernel/resource/environment tables and command block

### D024 AIX Setup

The English AIX guide covers the Korean source semantics for:

- AIX setup purpose, Altibase Configuration File Guide reference, AIX `5.x` basis, and AIX `4.3` exclusion
- Posix AIO requirement, disk I/O/application concurrency benefit, and AIX `6.1` `Available` default
- file cache rationale, AIX `5.2 ML03`/`6.1` applicability, AIX stealing behavior, `minperm`, `lru_file_repage`, and `strict_maxclient`
- AIX resource-limit kernel row for `Maximum number of PROCESSES allowed per user`
- `smit`, `vmo`, `lsdev -C | grep aio`, `vmo -p`, and `vmo -L` procedures
- user resource limits, open-files session caution, hard/soft limits, and `/etc/security/limits`
- AIX multithread variables, `PTHREAD_FORCE_SCOPE_SYSTEM` requirement, IBM website reference, and AIX 5.2+ `AIXTHREAD_MUTEX_FAST`
- summary kernel/resource/environment tables and command block
- AIX `heapmin` memory leak bug, IBM `IV28577` reference, `instfix -i | grep IV28577`, and latest patch recommendation
- AIX fixed `semume=1024` IPC channel limit and version-based maximum IPC channel counts: `512` before `5.1.5.72`, `341` for `5.1.5.72 or later`

The Korean source states that `PTHREAD_FORCE_SCOPE_SYSTEM` must be set but does not provide a value in the AIX example. The English guide preserves the requirement. This is a source limitation in the example content, not an unresolved KO/EN discrepancy.

### D057 Linux Setup

The English Linux guide covers the Korean source semantics for:

- Linux setup purpose, Altibase `5.5.1 or later`, and Red Hat Enterprise Linux `6 or later`
- glibc compatibility matrix across Altibase versions, Oracle Linux/RHEL/CentOS/Rocky/Ubuntu/POWER rows, and version notes
- glibc recommended version rationale and `rpm -q glibc`
- CPU frequency Governor, RemoveIPC, swappiness, THP, max_map_count, shared memory, and semaphore recommendations
- CPUfreq `cat`, `cpupower`, RHEL 6/7 driver checks, per-core clock checks, temporary changes, and persistent `rc.local`, `udev`, and `tuned` methods
- RemoveIPC check and persistent `/etc/systemd/logind.conf` update
- swappiness checks and changes, including RHEL 8 `vm.force_cgroup_v2_swappiness`, cgroup `memory.swappiness`, Red Hat Solution `6785021`, and tuned handling
- THP checks and changes, including RHEL 6/7 paths, `/proc/meminfo`, `/proc/cmdline`, `transparent_hugepage=never`, `transparent_hugepage.defrag=never`, GRUB, rc.local, and tuned `[vm]`
- max_map_count checks and changes, including sysctl, rc.local, and tuned `[sysctl]`
- shared memory and semaphore checks and changes through `ipcs`, `sysctl`, `/proc/sys/kernel/*`, and `/etc/sysctl.conf`
- user resource limits, related errors, `ulimit`, process limits, hard/soft limits, and `/etc/security/limits.conf`
- environment variables, `MALLOC_ARENA_MAX`, `ALTIBASE_NLS_USE`, `LANG`, charset query through `V$NLS_PARAMETERS`, and `.bash_profile` examples
- summary table for kernel parameters, IPC resources, OS user limits, and environment variables
- RHEL swap-size notes, systemd timeout risk during startup, SEP SYS CPU usage warning, reference links, and two Korean-source PDF attachment links

## Attachment Evidence

URL-backed document-format attachments in this scope:

- `202312_Altibase_디스크IO_병목을_고려한_볼륨구성_가이드.pdf`: preserved in `arch/Home/Configuration Guide For Minimizing Disk I_O Contention__22643018.md`
- `201511_ALTIBASE_디스크IO_병목을_고려한_볼륨구성_가이드.pdf`: preserved in `arch/Home/Configuration Guide For Minimizing Disk I_O Contention__22643018.md`
- `200912_ALTIBASE_디스크IO_병목을_고려한_볼륨구성_가이드.pdf`: preserved in `arch/Home/Configuration Guide For Minimizing Disk I_O Contention__22643018.md`
- `Altibase_운영을_위한_Linux_설정_가이드_2019.pdf`: preserved in `arch/Home/Linux Setup Guide for Altibase__22643022.md`
- `ALTIBASE_운영을_위한_Linux_설정_가이드.pdf`: preserved in `arch/Home/Linux Setup Guide for Altibase__22643022.md`

The Solaris, HPUX, and AIX scoped Korean pages contain no URL-backed document-format attachments. The AIX IBM `IV28577` external reference URL is preserved in English.

## Self-Review

- Scope checked: only S004 evidence files and the S004 workflow status were changed.
- Korean authority checked: all five Korean source files were inspected directly with line-numbered reads.
- English target checked: all eight English target files were inspected directly with line-numbered reads.
- Matrix checked: the S004 matrix uses the exact required TSV header, one physical row per matrix unit, allowed status values only, and no `missing`, `unverified`, or `recheck_required` rows.
- Coverage checked: commands, kernel parameters, environment variables, version conditions, OS paths, error messages, external links, and PDF attachment links were included in matrix evidence.
- Product docs checked: no English source change was needed, so `manifest.json` metadata remained valid and unchanged.
- Known source quirks handled: Korean legal/warranty boilerplate and contact-only support boilerplate are `not_applicable`; Korean export/table artifacts and typos such as `[vml]` were evaluated against the intended technical meaning already represented in English.

## Verification

Verification results after drafting and self-review:

| Check | Result |
| --- | --- |
| `python3 -m json.tool manifest.json >/tmp/aid-manifest-check.json` | Passed |
| `git diff --check` | Passed |
| `find DOCK/Home -type f -name '*.md' \| wc -l` | 51 |
| `find faq/Home -type f -name '*.md' \| wc -l` | 115 |
| `find arch/Home -type f -name '*.md' \| wc -l` | 181 |
| `find FAQE/Home -type f -name '*.md' \| wc -l` | 241 |
| S004 TSV header and column-count check | Passed: 106 data rows, 15 columns each |
| S004 coverage status check | Passed: 91 `covered`, 15 `not_applicable` |
| S004 unresolved-status scan | Passed with exit code 1, meaning no `missing`, `unverified`, or `recheck_required` rows |
| Scoped empty-link and macro-artifact scan over S004 English targets and evidence | Passed with exit code 1, meaning no matches |
| Scoped attachment preservation grep | Passed: 5 URL-backed PDF attachment links preserved |

## Decision

S004 is complete for its scoped semantic-unit audit.

S004 final decision: `COMPLETE`.
