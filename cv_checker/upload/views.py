from django.shortcuts import render
from .models import uploadCV, Rematch
from .utils import extract_text_from_pdf, compare_cvs, keyword_ats


def rematch_cv(request):
    if request.method == "POST" and request.FILES.get("user_cv"):
        user_file = request.FILES["user_cv"]
        ideal_text_input = request.POST.get("ideal_text")  

        # Save user CV
        user_cv = uploadCV.objects.create(cv_file=user_file)
        user_text = extract_text_from_pdf(user_cv.cv_file.path)
        user_cv.extracted_text = user_text

        # Decide mode: Ideal text match or Keyword match
        if ideal_text_input and ideal_text_input.strip():
            ideal_obj = Rematch.objects.create(ideal_text=ideal_text_input)

            score, matched, missing = compare_cvs(user_text, ideal_text_input)
            mode = "Ideal Text Match"

            ideal_obj.ats_score = score
            ideal_obj.save()
        else:
            score, matched, missing = keyword_ats(user_text)
            mode = "Keyword Match"

        user_cv.ats_score = score
        user_cv.save()

        return render(request, "upload/result.html", {
            "score": score,
            "matched": matched,
            "missing": missing,
            "mode": mode,
        })

    return render(request, "upload/rematch.html")
