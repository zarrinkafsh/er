(function(t) {
    function e() {
        var e = t(this).closest(".wrapper-row-editor").find("table").attr("id");
        console.log(e);
        var d = t("#" + e).DataTable();
        d.row.add([t(this).val(), t(this).val(), t(this).val(), t(this).val(), t(this).val(), t(this).val()]).draw()
    }
    t.fn.mdbEditor = function() {
        return this.each(function() {
            function e() {
                k.on("click", ".buttonAdd", d), m.on("click", "tr", l), m.on("click", "tr", o), y.on("click", C, a), y.on("click", C, i), x.on("click", ".btnYesClass", p), E.on("click", N, s), E.on("click", N, n), E.on("click", N, r), E.on("click", N, c)
            }

            function d() {
                w.row.add([b.find(".addNewInputs input").eq(0).val(), b.find(".addNewInputs input").eq(1).val(), b.find(".addNewInputs input").eq(2).val(), b.find(".addNewInputs input").eq(3).val(), b.find(".addNewInputs input").eq(4).val(), b.find(".addNewInputs input").eq(5).val()]).draw()
            }

            function l() {
                t(this).not("thead tr").not("tfoot tr").toggleClass("tr-color-selected").siblings().removeClass("tr-color-selected")
            }

            function o() {
                f = this, t(this).not("thead tr").not("tfoot tr").hasClass("tr-color-selected") ? (C.prop("disabled", !1), q.prop("disabled", !1), h.html("1 row selected")) : t("tr").hasClass("tr-color-selected") || (C.prop("disabled", !0), q.prop("disabled", !0), h.html("0 row selected"))
            }

            function a() {
                w.row(b.find(".modalEditClass input").eq(0).val(w.cell(f, 0).data()), b.find(".modalEditClass input").eq(1).val(w.cell(f, 1).data()), b.find(".modalEditClass input").eq(2).val(w.cell(f, 2).data()), b.find(".modalEditClass input").eq(3).val(w.cell(f, 3).data()), b.find(".modalEditClass input").eq(4).val(w.cell(f, 4).data()), b.find(".modalEditClass input").eq(5).val(w.cell(f, 5).data()))
            }

            function i() {
                t(".modalEditClass label").addClass("active")
            }

            function s() {
                w.cell(t(I).find("td").eq(0)).data(b.find(".modalEditClass input").eq(0).val()), w.cell(t(I).find("td").eq(1)).data(b.find(".modalEditClass input").eq(1).val()), w.cell(t(I).find("td").eq(2)).data(b.find(".modalEditClass input").eq(2).val()), w.cell(t(I).find("td").eq(3)).data(b.find(".modalEditClass input").eq(3).val()), w.cell(t(I).find("td").eq(4)).data(b.find(".modalEditClass input").eq(4).val()), w.cell(t(I).find("td").eq(5)).data(b.find(".modalEditClass input").eq(5).val())
            }

            function n() {
                u.find(".tr-color-selected").removeClass("tr-color-selected")
            }

            function r() {
                C.prop("disabled", !0), q.prop("disabled", !0)
            }

            function c() {
                h.html("0 row selected"), w.draw(!1)
            }

            function p() {
                C.prop("disabled", !0), q.prop("disabled", !0), h.html("0 row selected"), w.row(t(I)).remove().draw()
            }
            var f, u = t(this),
                v = u.closest(".wrapper-modal-editor").find("table").attr("id"),
                m = t("#" + v),
                w = t("#" + v).DataTable(),
                b = m.closest(".wrapper-modal-editor"),
                h = b.find(".createShowP"),
                C = b.find(".buttonEdit"),
                q = b.find(".buttonDelete"),
                k = b.find(".buttonAddFormWrapper"),
                y = b.find(".buttonEditWrapper"),
                E = b.find(".editInsideWrapper"),
                x = b.find(".deleteButtonsWrapper"),
                N = b.find(".editInside"),
                I = ".tr-color-selected";
            e()
        })
    }, t.fn.mdbEditorRow = function() {
        return this.each(function() {
            function e() {
                q.on("click", C, d), q.on("click", C, l), m.on("click", p, o), m.on("click", p, a), m.on("click", p, i), m.on("click", f, s), m.on("click", f, n), t(".buttonYesNoWrapper").on("click", ".btnYes", r), q.on("click", ".removeColumns", c)
            }

            function d() {
                var e = t(this).closest(".wrapper-row-editor").find("table").attr("id");
                t(document).find("#" + e).each(function() {
                    t(this).find("tr").each(function() {
                        t(this).find(u).not(".td-editor").after('<td class="text-center td-editor" style="border-top: 1px solid #dee2e6; border-bottom:1px solid #dee2e6"><button class="btn btn-sm editRow btn-sm btn-teal"><i class="far fa-edit"></i></button></td>')
                    })
                })
            }

            function l() {
                var e = t(this).closest(".wrapper-row-editor").find("table").attr("id"),
                    d = t("#" + e).closest(".wrapper-row-editor").find(".removeColumns");
                1 == t("#" + e).find("td").hasClass("td-editor") ? d.prop("disabled", !1) : d.prop("disabled", !0), t("#" + e).closest(".wrapper-row-editor").find("td.td-editor").hasClass("td-editor") || d.prop("disabled", !0)
            }

            function o() {
                var e = t(this).closest("tr").find("td"),
                    d = t(this).closest("tr").find(p),
                    l = e.eq(0).html(),
                    o = e.eq(1).html(),
                    a = e.eq(2).html(),
                    i = e.eq(3).html(),
                    s = e.eq(4).html(),
                    n = e.eq(5).html(),
                    r = '<input type="text" class="val1 form-control" value="' + l + '" >',
                    c = '<input type="text" class="val2 form-control" value="' + o + '" >',
                    f = '<input type="text" class="val3 form-control" value="' + a + '" >',
                    u = '<input type="number" class="val4 form-control" value="' + i + '" >',
                    v = '<input type="text" class="val5 form-control" value="' + s + '" >',
                    m = '<input type="text" class="val6 form-control" value="' + n + '" >',
                    b = '<td class="text-center td-editor td-yes" style="border:none"><button class="btn btn-sm btn-danger deleteRow" style="cursor:pointer;"><i class="fas fa-trash-alt"></i></b></td>',
                    h = '<td class="text-center td-editor td-yes" style="border:none"><button class="btn btn-sm btn-primary saveRow" style="cursor:pointer;"><i class="fas fa-check"></i></button></td>';
                e.eq(0).html(r), e.eq(1).html(c), e.eq(2).html(f), e.eq(3).html(u), e.eq(4).html(v), e.eq(5).html(m), d.after(b), d.after(h), t(t("#" + w)).on("click", ".deleteRow", function() {
                    var e = t(this).closest(".wrapper-row-editor").find("table").attr("id");
                    t(t("#" + e).closest(".wrapper-row-editor").find(".showForm").removeClass("d-none")), t(t("#" + e)).closest(".wrapper-row-editor").find(".closeByClick").removeClass("d-none")
                })
            }

            function a() {
                var e = t(this).closest("tr");
                e.addClass("tr-color-selected"), e.find("td").not(".td-editor").addClass("py-5")
            }

            function i() {
                var e = t(this).closest(".wrapper-row-editor");
                t(this).prop("disabled", !0), t(e).find(v).prop("disabled", !0)
            }

            function s() {
                var e = t(this).closest("tr").find("td"),
                    d = t(this).closest("tr");
                h.cell(e.eq(0)).data(d.find(".val1").val()), h.cell(e.eq(1)).data(d.find(".val2").val()), h.cell(e.eq(2)).data(d.find(".val3").val()), h.cell(e.eq(3)).data(d.find(".val4").val()), h.cell(e.eq(4)).data(d.find(".val5").val()), h.cell(e.eq(5)).data(d.find(".val6").val()), d.find("td").removeClass("py-5")
            }

            function n() {
                var e = t(this).closest(".wrapper-row-editor").find("table").attr("id"),
                    d = t(this).closest("tr");
                d.find(p).prop("disabled", !1), d.removeClass("tr-color-selected"), d.find(".td-yes").remove(), h.draw(!1), t("#" + e).closest(".wrapper-row-editor").find(".removeColumns").prop("disabled", !1)
            }

            function r() {
                var e = t(this).closest(".wrapper-row-editor").find("table").attr("id");
                h.row(t("#" + e).find("tr.tr-color-selected")).remove().draw(!1), t("#" + e + " tr").hasClass("td-editor") ? t("#" + e).closest(".wrapper-row-editor").find(v).prop("disabled", !0) : t("#" + e).closest(".wrapper-row-editor").find(v).prop("disabled", !1)
            }

            function c() {
                var e = t(this).closest(".wrapper-row-editor").find("table").attr("id"),
                    d = t(this).closest(".wrapper-row-editor");
                !t("#" + e).hasClass("td-editor") == !0 && d.find(".removeColumns").attr("disabled", !0), t("#" + e).hasClass("td-editor") === !1 && t("#" + e + " tr").hasClass("tr-color-selected") === !1 && (t("#" + e).find(".td-editor").remove(), t("#" + e).find(".tr-color-selected").remove(), h.draw(!1))
            }
            var p = ".editRow",
                f = ".saveRow",
                u = "td:last",
                v = t(".removeColumns"),
                m = t(this),
                w = t(this).closest(".wrapper-row-editor").find("table").attr("id"),
                b = t("#" + w),
                h = b.DataTable(),
                C = ".addNewColumn",
                q = t(".buttonWrapper"),
                k = t(".closeByClick"),
                y = t(".showForm");
            e(), k.hasClass("d-none") === !0 && t(document).keyup(function(t) {
                27 === t.keyCode && (k.addClass("d-none"), y.addClass("d-none"))
            }), k.on("click", function() {
                t(this).addClass("d-none"), y.addClass("d-none")
            }), y.on("click", ".btnYes, .button-x, .btnNo", function() {
                y.addClass("d-none"), k.addClass("d-none")
            })
        })
    }, t(".buttonWrapper").on("click", ".addNewRows", e)
})(jQuery);
