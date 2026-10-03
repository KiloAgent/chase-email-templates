const FIELD = /\{\{([a-z0-9_]+)\}\}/g;
const UNCLOSED = /\{\{(?![^{}]*\}\})/;

/**
 * Replace {{field}} tokens. Throws on an unknown field or an unclosed brace.
 * @param {string} template
 * @param {Record<string, string | number>} fields
 * @returns {string}
 */
export function merge(template, fields) {
  if (typeof template !== "string") {
    throw new Error("template must be a string");
  }
  if (UNCLOSED.test(template)) {
    throw new Error("unclosed brace");
  }
  return template.replace(FIELD, (_match, key) => {
    if (!Object.hasOwn(fields, key)) {
      throw new Error(`unknown field ${key}`);
    }
    return String(fields[key]);
  });
}

/**
 * True when a rendered string still has `{` or `}`.
 * @param {string} text
 */
export function hasLeftoverBraces(text) {
  return text.includes("{") || text.includes("}");
}
