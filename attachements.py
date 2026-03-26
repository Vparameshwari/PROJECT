function myFunction() {
  var folder = DriveApp.getFolderById("1GbSQPHSvHHVpuBOOnBSBMCv64nMpgJXn");
  var threads = GmailApp.search("has:attachment is:unread");

  threads.forEach(function(thread) {
    var messages = thread.getMessages();

    messages.forEach(function(message) {
      var attachments = message.getAttachments();

      attachments.forEach(function(file) {
        folder.createFile(file);
      });

      message.markRead(); // mark message as read
    });
  });
}
