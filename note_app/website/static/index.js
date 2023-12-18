function deleteNote(noteId) {
  //we send request in js by using fetch
  fetch("/delete-note", {
    method: "POST",
    body: JSON.stringify({ noteId: noteId }),
  }).then((_res) => {
    //after job done on delete-note it will go to page with route '/'(home)
    window.location.href = "/";
  });
}
