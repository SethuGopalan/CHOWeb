(function (w, d, x, id) {
  s = d.createElement("script");
  s.src =
    "https://dtn7rvxwwlhud.cloudfront.net/amazon-connect-chat-interface-client.js";
  s.async = 1;
  s.id = id;
  d.getElementsByTagName("head")[0].appendChild(s);
  w[x] =
    w[x] ||
    function () {
      (w[x].ac = w[x].ac || []).push(arguments);
    };
})(window, document, "amazon_connect", "4dc53720-d8a7-4a3f-b9f0-155b1262528b");
amazon_connect("styles", {
  openChat: { color: "#ffffff", backgroundColor: "#123456" },
  closeChat: { color: "#ffffff", backgroundColor: "#123456" },
});
amazon_connect(
  "snippetId",
  "QVFJREFIakZhMVo2ZGZmSXpGSnpJS2lYakthYVBxMmJIU0ZPbnhET3AyalJDV1F3UWdHWklDNXZCL09na2xFUXZUY3lyandVQUFBQWJqQnNCZ2txaGtpRzl3MEJCd2FnWHpCZEFnRUFNRmdHQ1NxR1NJYjNEUUVIQVRBZUJnbGdoa2dCWlFNRUFTNHdFUVFNRlR2c3JhUG5aTzZrcCtteUFnRVFnQ3UxdTdXUGY4cmh1cVJJVkhEQUlnUmdXZC9udU9jK1BTV3l2ZU9XaHJsTm4yZy80SXQ1b2U3dkd3aEQ6OjFuRFFVc3AyamJOeHZzbU1UVm1vUFpFSDBIQWNibFU2enNJdG5sb01MNWxvYzhWTkFjcmZGQVdIYy9HQ2JTRjFrUDd2eXMwMXdjQmJKcXNEcTNiYVltbXJ0M2xQOTBJcmFuUnp5SVdhaVhNU2sxNHk5cDFSVW04Uy8rOEF5NHZPSXBQWUQwc1FQQlBnQ1MrT2ZMZk9mQ3FuS3pYZDFNMD0="
);
amazon_connect("supportedMessagingContentTypes", [
  "text/plain",
  "text/markdown",
]);
// </script>
