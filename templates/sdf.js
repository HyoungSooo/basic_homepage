const p = document.querySelectorAll(".dumy");
const p_body = document.querySelectorAll(".dumy-body");

const id_head = "accordion-color-heading-";
const id_body = "accordion-color-body-";

for (let i = 0; i < p.length; i++) {
  const element = p[i];
  element.id = id_head + i;
}
