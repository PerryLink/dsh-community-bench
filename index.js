/**
 * Host half of the Community Bench consumer. It registers nothing: the tab is
 * a pure Client view over the public registry, so there is no local score and
 * no model-facing tool to keep in sync.
 *
 * @module dsh-community-bench
 */

export const name = 'dsh-community-bench'

/** No Host service is required. */
export function apply() {}
